import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import BlankScreen5303Navigator from '../features/BlankScreen5303/navigator';
import BlankScreen4964Navigator from '../features/BlankScreen4964/navigator';
import BlankScreen4808Navigator from '../features/BlankScreen4808/navigator';
import BlankScreen4633Navigator from '../features/BlankScreen4633/navigator';
import EmailAuthNavigator from '../features/EmailAuth/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {
    SplashScreen: {
      screen: SplashScreen
    },
    //@BlueprintNavigationInsertion
BlankScreen5303: { screen: BlankScreen5303Navigator },
BlankScreen4964: { screen: BlankScreen4964Navigator },
BlankScreen4808: { screen: BlankScreen4808Navigator },
BlankScreen4633: { screen: BlankScreen4633Navigator },
EmailAuth: { screen: EmailAuthNavigator },

    /** new navigators can be added here */
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu,
    initialRouteName: 'SplashScreen',
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
