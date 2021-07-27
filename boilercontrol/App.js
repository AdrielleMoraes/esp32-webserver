import React from 'react';
import { View, Text, Image, ScrollView, TextInput } from 'react-native';
import Cat from './Components/Cat';
const App = () => {
  return (
    <ScrollView>
      <Text>Some text</Text>
      <View>
        <Text>Some more text</Text>
        <Cat name="Furry"/>
      </View>
      <TextInput
        style={{
          height: 40,
          borderColor: 'gray',
          borderWidth: 1
        }}
        defaultValue="You can type in me"
      />
    </ScrollView>
  );
}

export default App;