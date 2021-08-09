import React from 'react';
import {Button} from 'react-native';

const HomeScreen = ({ navigation }) =>{
    return (
      <Button
        title="Go to your profile"
        onPress={() =>
          navigation.navigate('Profile', { name: 'Adrielle' })
        }
      />
    );
  };

export default HomeScreen;