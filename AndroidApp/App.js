import React from 'react';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack'
import HomeScreen from './components/HomeScreen/HomeScreen'
import ProfileScreen from './components/ProfileScreen/ProfileScreen'
import Sensor from './components/Sensor/Sensor'

const Stack = createStackNavigator()

const App = () => {
  return (
    <NavigationContainer>
       <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{ title: 'Welcome' }}
        />
        <Stack.Screen name="Profile" component={ProfileScreen} />
        <Stack.Screen name="Sensor" component={Sensor} />
      </Stack.Navigator>
    </NavigationContainer>
  )
}

export default App
