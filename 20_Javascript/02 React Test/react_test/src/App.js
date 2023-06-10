import './App.css';

import Nav from './components/Nav';
import Promo from './components/Promo';
import Intro1 from './components/Intro1';
import Footer from './components/Footer';

// for props.children
import Bag from './components/Bag';
import Apples from './components/Bag_children/Apples';
import Pears from './components/Bag_children/Pears';

// for Hooks
import ModeToggler from './components/ModeToggler';
import InputComponent from './components/InputComponent';

// Calculator project
import Calculator from './components/Calculator/Calculator';

// Form
import Form from './components/Form/Form';

// Lifting up state
import MyApp from './components/Lifting_Up/MyApp';

// Async Promise
import AsyncPromise from './components/Async_Promise/AsyncPromise';
import AsyncForm from './components/Async_Promise/AsyncPromise_form';
import FeedbackForm from './components/Async_Promise/AsyncPromise_form1';

// Nested Tree
import TravelPlan from './components/NestedTree/TravelPlan';

// Lift Up State + Search List
import FilterableList from './components/LiftUpState/SearchList';

// Reducer
import Messenger from './components/Reducer1/Messenger';
import TaskApp from './components/Reducer2/TaskApp';

// Context - to pass props without prop drilling
import ImageApp from './components/Context/ImageApp';
import Page from './components/Context1/Page';

// useRef to access DOM
import CatFriends from './components/useRef_DOM/CatFriends';

function App(props) {
  return (
    <div className="App">
      <h1>{props.title}</h1>

      <Nav />

      <Promo heading="Welcome to my website!" promoSubHeading="This is a subheading." />
      <Intro1 />
      <Footer />

      {/* props.children used here */}
      <Bag>
        <Apples color="yellow" number="5" />
        <Pears friend="Peter" />
      </Bag>

      <ModeToggler /> <hr />
      
      <InputComponent />

      <Calculator />

      <Form /> <hr />

      <MyApp /> <hr />

      <AsyncPromise /> <hr />

      <AsyncForm /> <hr />

      <FeedbackForm /> <hr />

      <TravelPlan /> <hr />

      <FilterableList /> <hr />

      <Messenger /> <hr />

      <TaskApp /> <hr />

      <ImageApp /> <hr />

      <Page /> <hr />

      <CatFriends /> <hr />

    </div>
  );
}

export default App;
