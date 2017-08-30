from rest_framework import serializers

from . models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ('id', 'firstname', 'lastname')
   
    def validate_firstname(self, value):
    	if 'john' not in value.lower():
    		raise serializers.ValidationError('First name must be John')
    	return value

    def validate_lastname(self, value):

    	if 'smith' in value.lower():
    		raise serializers.ValidationError("Last name can't be Smith")
    	return value

    def validate(self, data):
    	if data['firstname'] == 'John' and data['lastname'] == 'Doe':
    		raise serializers.ValidationError("Please enter a more original name")