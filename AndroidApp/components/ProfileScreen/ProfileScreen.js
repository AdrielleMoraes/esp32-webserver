import React from 'react';
import {View, Text, Button} from 'react-native';
import {Avatar} from 'react-native-elements';

const ProfileScreen = ({navigation, route}) => {
  return (
    <View>
      <Avatar
        rounded
        size="medium"
        title="AM"
        activeOpacity={0.7}
        overlayContainerStyle={{backgroundColor: 'green'}}
      />
      <Text>This is {route.params.name}'s profile</Text>
      <Button
              title="Sensor"
              onPress={() => navigation.navigate('Sensor')}
            />
      <Text>Connected sensors</Text>
    </View>
  );
};

export default ProfileScreen;