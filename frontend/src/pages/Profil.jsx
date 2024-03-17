import React, { Component } from 'react';
import Eigenschaften from '../componnents/Profile/Eigenschaften';
import Profildaten from '../componnents/Profile/Profildaten';
import "./Matchpage.css";

class Profil extends Component {
    constructor(props) {
      super(props)

      this.state = {

      }
    }

    handleIsSaved = (isSaved) => {
        this.props.handleIsSaved(isSaved)
      };

    handleFirstnameSaved = (savedFirstname) => {
        this.props.handleFirstnameSaved(savedFirstname)
      };

    render() {
        return (
            <div className='section-profile'>
                <Profildaten handleFirstnameSaved={this.handleFirstnameSaved} user={this.props.user}></Profildaten>
                <Eigenschaften user={this.props.user} isSearchprofile={false} profile={this.props.user} handleIsSaved={this.handleIsSaved}/>
            </div>
        );
    }
}
export default Profil;