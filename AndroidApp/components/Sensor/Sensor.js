import React, {useState} from 'react'
import {View, Text} from 'react-native'
import styles from './Sensor.component.style.android'
import { ListItem, Switch } from 'react-native-elements'

const Sensor = ({navigation, route}) => {
    const [statusButton, setStatusButton] = useState(false)

    const ToggleButton = () => {
        let old_state = statusButton
        setStatusButton(!old_state)
    }
    return (
        <View>
            <View style={styles.container}>
                <Text>Sensor {route.params.name}</Text>
            </View>
            <View>
                <ListItem key={0} bottomDivider onPress={ToggleButton}>
                    <ListItem.Content>
                    <ListItem.Title>{statusButton? 'On':'Off'}</ListItem.Title>
                    </ListItem.Content>
                    <Switch value={statusButton} onValueChange={ToggleButton}/>
                </ListItem>
                <ListItem key={1} bottomDivider>
                    <ListItem.Content>
                    <ListItem.Title>Temperature</ListItem.Title>
                    </ListItem.Content>
                    <ListItem.Chevron />
                </ListItem>
            </View>
        </View>
    )
  }

  export default Sensor