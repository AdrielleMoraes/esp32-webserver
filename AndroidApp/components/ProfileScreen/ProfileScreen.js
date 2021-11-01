import React from 'react';
import {View, Text, Button} from 'react-native';
import {Avatar} from 'react-native-elements';
// import HookMqtt from '../MQTT/MQTT_client'


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
      
      <HookMqtt/>
      
      <Button
              title="Sensor"
              onPress={() => navigation.navigate('Sensor', {name: 'Esp32'})}
            />
      <Text>Connected sensors</Text>
    </View>
  );
};

export default ProfileScreen;
