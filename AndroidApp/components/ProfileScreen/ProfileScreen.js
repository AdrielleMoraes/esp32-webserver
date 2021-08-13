import React from 'react';
import {View, Text} from 'react-native';
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
      <Text>Connect to Sensor</Text>
      <Text>Connected sensors</Text>
    </View>
  );
};

export default ProfileScreen;
