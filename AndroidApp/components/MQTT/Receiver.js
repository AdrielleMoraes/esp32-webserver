import React, { useEffect, useState } from 'react';
import {View, Button, Text} from 'react-native'

const Receiver = ({ payload }) => {
  const [messages, setMessages] = useState([])

  useEffect(() => {
    if (payload.topic) {
      setMessages(messages => [...messages, payload])
    }
  }, [payload])

//   const renderListItem = (item) => (
//     <List.Item>
//       <List.Item.Meta
//         title={item.topic}
//         description={item.message}
//       />
//     </List.Item>
//   )

  return (
    <View>
      {/* <List
        dataSource={messages}
        renderItem={renderListItem}
      /> */}
    </View>
  );
}

export default Receiver;