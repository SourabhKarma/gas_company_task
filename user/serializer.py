
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .manager import UserManager










class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()


    def create(self, validated_data):

        user = User.objects.create_user(
            # username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],

        )

        return user
        
    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "password", "email","is_verified")




class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'password',
        )
    # def create(self, validated_data):
    #     auth_user = User.objects.create_user(**validated_data)
    #     return auth_user

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user









# login


class UserLoginSerializer(serializers.Serializer):
    # username = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    user_id = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        # username = data['username']
        email = data['email']
        password = data['password']
        print(email)
        print(password)
        User = authenticate(email= email, password=password)

        if User is None:
            raise serializers.ValidationError("Invalid login")

        try:
            refresh = RefreshToken.for_user(User)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None, User)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': User.email,
                # 'user_id':User.id,
            }

            return validation
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")














#-------------------------------------- user account -----------------------------------


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields= ("__all__")









#--------------------------------------user account end --------------------------------










