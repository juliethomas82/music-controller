import React, { Component } from "react";
import { render } from "react-dom";
import Homepage from "./Homepage";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <Homepage />
            </div>
        );
    }
}

const appDiv = document.getElementById("app");
render(<App />, appDiv);


// import React, { Component } from "react";
// import { render } from "react-dom";

// export default class App extends Component {
//     constructor(props) {
//         super(props);
//     }

//     render() {
//         return <h1>{this.props.name}</h1>
//     }
// }

// const appDiv = document.getElementById("app");
// render(<App name="julie"/>, appDiv);
