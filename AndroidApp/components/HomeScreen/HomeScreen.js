import React from 'react'
import {Button, View} from 'react-native'

const HomeScreen = ({navigation}) => {
  return (
          <View>
            <Button
              title="Start"
              onPress={() => navigation.navigate('Profile', {name: 'Adrielle'})}
            />
            <Button
              title="Sensor"
              onPress={() => navigation.navigate('Sensor')}
            />
      </View>
  )
}
export default HomeScreen