import React, {useState} from 'react'
import {View, Image, Text, TextInput, Button} from 'react-native'

const Cat = props => {
  let cat_pic0 = 'https://images.unsplash.com/photo-1511275539165-cc46b1ee89bf?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjN8fGNhdHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
  let cat_pic1= 'https://images.unsplash.com/photo-1548247416-ec66f4900b2e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=363&q=80'
  const [isHungry, setIsHungry] = useState(true)
  const [catName, setCatName] = useState("Kitty")
  return (
      <View style={{padding: 10}}>
        <TextInput
          style={{height: 40}}
          placeholder="Type here to name your cat!"
          onChangeText={catName => setCatName(catName)} 
          defaultValue={catName}
        />
        <Text>
          Hello, I am your cat {catName}! {props.name}, and I am{' '}
          {isHungry ? 'hungry' : 'full'}!
        </Text>
        <Image
          source={{
            uri: isHungry ? cat_pic1 : cat_pic0,
          }}
          style={{width: 200, height: 200}}
        />
        <Button
          onPress={() => {
            setIsHungry(false)
          }}
          disabled={!isHungry}
          title={isHungry ? 'Pour me some milk, please!' : 'Thank you!'}
        />
      </View>
  )
}
export default Cat
