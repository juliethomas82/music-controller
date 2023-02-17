import React, { Component } from 'react';
import RoomJoinPage from './RoomJoinPage';
import CreateRoomPage from './CreateRoomPage';
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom";

export default class Homepage extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
          <Router>
            <Routes>
              <Route path="/" element={<p>This is the HomePage</p>} />
              <Route path="/join/*" element={<RoomJoinPage />} />
              <Route path="/create" element={<CreateRoomPage />} />
            </Routes>
          </Router>
        );
      }

    // render() {
    //     return <Router>
    //         <Routes>
    //             <Route exact path='/'>
    //                 <p>This is the Homepage</p>;
    //             </Route>
    //             <Route path='/join' component={RoomJoinPage}></Route>
    //             <Route path='/create' component={CreateRoomPage}></Route>
    //         </Routes>
    //     </Router>
    // }
}