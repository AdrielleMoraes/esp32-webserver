import React from 'react';
import {View, ScrollView} from 'react-native';
import Cat from './Components/Cat';

const App = () => {
  return (
    <ScrollView>
      <View>
        <Cat name="Furry" />
      </View>
    </ScrollView>
  );
};

export default App;
