from rest_framework import serializers
from django_redis import get_redis_connection
from .models import User
import re

class CreateUserSerializer(serializers.ModelSerializer):
    '''
    username: 3-20, and only contain alphanumeric characters
    password and password2 must be the same.3-20 characters
    email
    email verification code
    check the agreement - alllow
    '''
    password2 = serializers.CharField(label='Confirm password', write_only=True)
    sms_code = serializers.CharField(label='Email Verification Code', write_only=True)
    allow = serializers.CharField(label='agree', write_only=True)
    token = serializers.CharField(label='Token', read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'sms_code', 'email', 'allow', 'token', 'mobile')
        extra_kwargs = {'password': {'write_only': True,
                                     'min_length': 3,
                                     'max_length': 20,
                                     'error_messages': {
                                         'min_length': 'Length must be at least 3 characters',
                                         'max_length': 'Length must be at most 20 characters'
                                     }
                        },
                        'username': {'required':True,
                                     'min_length': 3,
                                     'max_length': 20,
                                     'error_messages': {
                                         'min_length': 'Length must be at least 3 characters',
                                         'max_length': 'Length must be at most 20 characters'
                                     }
                        }
        }
    def validate_username(self, username):
        regex = '[A-Za-z0-9_-]{3,20}'
        if not re.match(regex, username):
            raise serializers.ValidationError('only contains letters, numbers and underscores!')
        return username

    def validate_email(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not (re.fullmatch(regex, email)):
            raise serializers.ValidationError('Email is invalid!')
        return email

    def validate_allow(self, allow):
        if allow != 'true':
            raise serializers.ValidationError('Please check the agreement!')
        return allow
    def validate(self, attrs):
        if not attrs.get('password') or attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError('Password length cannot be 0 or Passwords do not match!')

        redis_conn = get_redis_connection('verify_codes')  # config in settings
        email = attrs.get('email').lower()
        # email_code = redis_conn.get(f'code_{email}')
        # if email_code is None:
        #     raise serializers.ValidationError('Verification code is invalid!')
        #
        # if attrs['sms_code'] != email_code.decode():  # front end emai code [sms_code] and redis email code compare
        #     raise serializers.ValidationError('Verification code is invalid!')
        return attrs

    def create(self, validated_data):
        """
        Create user and save
        deserializer data: validated_data
        """
        validated_data.pop('password2')
        validated_data.pop('allow')
        validated_data.pop('sms_code')

        user = User.objects.create_user(**validated_data)

        # server denerate a jwt token str, which use to save the user credential
        from rest_framework_jwt.settings import api_settings
        jwt_payload_hanler = api_settings.JWT_PAYLOAD_HANDLER  # generate payload
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  #  generate jwt token
        payload = jwt_payload_hanler(user)
        token = jwt_encode_handler(payload)

        # 给user对象增加属性token，保存生成jwt token数据
        user.token = token
        return user




