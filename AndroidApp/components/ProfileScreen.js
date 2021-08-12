import React from 'react';
import {View, Text, StyleSheet} from 'react-native';
import {Avatar} from 'react-native-elements';

const styles = StyleSheet.create({
  text: {
    fontSize: 24,
    textAlign: "center",
    marginHorizontal: 16,
    marginTop: 12,
  },
  blueText: {
    color: "blue",
  },
  greyText: {
    color: "grey",
  },
  image: {
    width: '100%',
    height: 300,
    backgroundColor: 'gray',
  },
});


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
      <Text>Conected sensors</Text>
      <View style={styles.image}></View>
    </View>
  );
};

export default ProfileScreen;
