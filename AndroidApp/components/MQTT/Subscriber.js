import React from 'react';
import {View, Button} from 'react-native'
import {MQTT_TOPIC_TEMP} from '@env'


const Subscriber = ({ sub, unSub, showUnsub }) => {
  const record = {
    topic: MQTT_TOPIC_TEMP,
  };

  const SubForm = (
    <View>
        <Button title= 'Subscribe' onPress={()=>sub(record.topic)}/>      
        {
        showUnsub ?
        <Button title="Unsubscribe" onPress={()=>unSub(record.topic)}/>
        : null
        }
    </View>
  )

  return (
    <View>
      {SubForm}
    </View>
  );
}

export default Subscriber;