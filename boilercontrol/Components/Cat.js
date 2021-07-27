import React from 'react';
import { View, Image, Text } from 'react-native';


const Cat = (props) => {
  return (
  <View>
      <Text>Hello, I am your cat! {props.name}</Text>
      <Image
        source={{
          uri: 'https://images.unsplash.com/photo-1548247416-ec66f4900b2e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=363&q=80',
        }}
        style={{ width: 200, height: 200 }}
      />
  </View>
  );
}

export default Cat;