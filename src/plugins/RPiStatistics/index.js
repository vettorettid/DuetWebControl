'use strict'

// import { registerSettingTab } from '../../routes'
import { registerRoute } from '../../routes'
//import { registerPluginData, PluginDataType } from '../../store'

import RPi from './RPiStatistics.vue'

// Register a route via Machine Settings -> Accelerometer
// registerSettingTab(false, 'RPi', RPi, 'plugins.rpi.name');

registerRoute(RPi, {
	Control: {
		RPi: {
			icon: 'mdi-memory',
			caption: 'SBC Info',
			path: '/RPi'
		}
	}
});

