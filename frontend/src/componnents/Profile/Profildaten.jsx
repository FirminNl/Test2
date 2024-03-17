import { Button, TextField } from '@mui/material';
import PropTypes from 'prop-types';
import React, { Component } from 'react';
import { UserProfileBO } from '../../api';
import UserProfileView from '../../api/Views/UserProfileView';
import { SuccessMessage } from '../constants';
import './Profildaten.css';

class Profildaten extends Component {
    constructor(props) {
      super(props)
        let fn = ""; let sr=""; let am=""; let fnS = false
        if(this.props){
                fn = this.props.user.getFirstname()
                sr = this.props.user.getSurname()
                am = this.props.user.getAboutMe()
                if(fn === ""){
                    fnS = true
                }
                this.props.handleFirstnameSaved(fnS)
            }

      this.state = {
         firstname:fn,
         surname:sr,
         aboutMe: am,
         success: false,
         error: false,
         fnSaved: fnS
      }
    }


     handleTextFieldChange = (event) => {
        this.setState({
          [event.target.id]: event.target.value,
        });
      };

      updateProfile = () => {
        let newProfileObject = Object.assign(this.props.user, UserProfileBO)
        newProfileObject.setFirstname(this.state.firstname)
        newProfileObject.setSurname(this.state.surname)
        newProfileObject.setAboutMe(this.state.aboutMe)
        UserProfileView.getView().update(newProfileObject).then((prof) =>
           { this.setState({
                success:true,
                error:false,
            })
            let fnS = this.state.firstname === "" ? true : false;
            this.props.handleFirstnameSaved(fnS)}
        )
        .catch(this.setState({
            error: true,
            success: false,
        }))
      }

     handleSuccessClose = () =>{
        this.setState({success:false})
     }


    render() {
        return (
            <div className='profildaten__container'>
                <div className="profildaten__header">
                    <h2 className="profildaten__header-h">Profildaten</h2>
                    <p className="profildaten__header-p">Erzähl uns doch mehr über dich</p>
                </div>
                <div className="profildaten__content">
                    <div className="profildaten__content-item">
                        <p className="profildaten__content-item-p">Vorname</p>
                        <TextField
                         id="firstname"
                         onChange={this.handleTextFieldChange}
                         value={this.state.firstname}
                         > </TextField>
                    </div>
                    <div className="profildaten__content-item">
                        <p className="profildaten__content-item-p">Nachname</p>
                        <TextField
                            id="surname"
                            onChange={this.handleTextFieldChange}
                            value={this.state.surname}></TextField>
                    </div>
                    <div className="profildaten__content-item">
                        <p className="profildaten__content-item-p">Über mich</p>
                        <TextField
                            id="aboutMe"
                            value={this.state.aboutMe}
                            onChange={this.handleTextFieldChange}
                            ></TextField>
                    </div>
                    <Button sx={{width:"fit-content", marginTop:"2rem"}} variant="contained" onClick={this.updateProfile}>Speichern</Button>
                    <SuccessMessage  successText="Erfolgreich gespeichert!" open={this.state.success} closeSuccess={this.handleSuccessClose}/>
                </div>
            </div>
        );
    }
}

Profildaten.propTypes = {

};

export default Profildaten;