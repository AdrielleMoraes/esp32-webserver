import React from 'react';
import {View, Button, Text} from 'react-native'
import {MQTT_BROKER, MQTT_USERNAME, MQTT_API} from '@env'

const Connection = ({ connect, disconnect, connectBtn }) => {
  const record = {
    host: MQTT_BROKER,
    clientId: `mqttjs_ + ${Math.random().toString(16).substr(2, 8)}`,
    username: MQTT_USERNAME,
    password: MQTT_API,
    port: 8083,
  };

  const handleConnect = () => {
    const options = {
      keepalive: 30,
      protocolId: 'MQTT',
      protocolVersion: 4,
      clean: true,
      reconnectPeriod: 1000,
      connectTimeout: 30 * 1000,
      will: {
        topic: 'WillMsg',
        payload: 'Connection Closed abnormally..!',
        qos: 0,
        retain: false
      },
      rejectUnauthorized: false
    };
    options.clientId = record.clientId;
    options.username = record.username;
    options.password = record.password;
    connect(options);
  };

  const handleDisconnect = () => {
    disconnect();
  };

  return (
    <View>
        <Text>{connectBtn}</Text>
        <Button title='Connect' onPress={handleConnect}/>
        <Button title='Disconnect' onClick={handleDisconnect}/>
    </View>
  );
}

export default Connection;