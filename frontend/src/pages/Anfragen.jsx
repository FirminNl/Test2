import { Button, CircularProgress, LinearProgress, Switch } from '@mui/material';
import React, { Component } from 'react';
import ChatView from '../api/Views/ChatView';
import MatchCard from '../componnents/Matching/MatchCard';


class Anfragen extends Component {
    constructor(props) {
      super(props)

      this.state = {
         isGesendeteAnfrage: false,
         isEmpfangeneAnfrage: false,
         requestList: [],
         loading: false
        }
    }

    handleSwitchChange = (event) => {
        this.getRequests(!this.state.isGesendeteAnfrage)
    }

    getRequests = (isGesendeteAnfrage) => {
        if(isGesendeteAnfrage){
            ChatView.getView().getBySentInvitation(this.props.user.getID()).then((inv) => {
                this.setState({
                    requestList: inv,
                    loading: false,
                    isGesendeteAnfrage: true
                })
            })
            .catch((err) => console.log("error", err));
            this.setState({
                requestList: [],
                loading: true
            })
        }
        else{
            ChatView.getView().getByInvitation(this.props.user.getID()).then((inv) => {
                this.setState({
                    requestList: inv,
                    loading: false,
                    isGesendeteAnfrage: false
                })
            })
            .catch((err) => console.log("error", err));
            this.setState({
                requestList: [],
                loading: true
            })
        }
    }

    removeEntry = (chat) => {
        this.setState({
            requestList: this.state.requestList.filter((item) => item.getID() !== chat.getID())
        })
    }

    componentDidMount(){
        this.getRequests()
    }
    render() {
        return (
            <div className='section-wrapper'>
                <div>
                    <h2 style={{color: "#E41036", margin:0}}>Anfragen</h2>
                    <p>Hier siehst du alle gesendeten und empfangenen Kontaktanfragen! </p>
                    <div className='anfragen-button-group'>
                        <p>Empfangene Anfragen</p>
                        <Switch
                        checked={this.state.isGesendeteAnfrage}
                        onChange={this.handleSwitchChange}
                        />
                        <p>Gesendete Anfragen</p>
                    </div>
                </div>
                {!this.state.loading ?
                <div className="section-card-grid">
                {this.state.requestList.map((item) =>
                 <MatchCard key={item.getID()}
                 parentComponent={this.state.isGesendeteAnfrage ? "gesendeteAnfrage" :"empfangeneAnfrage"}
                 parentObject={item}
                 candidateID={this.props.user.getID() === item.getSenderId() ? item.getReceiverId() : item.getSenderId()}
                 user={this.props.user}
                 removeEntry={this.removeEntry}/>)}
                </div>:
                <LinearProgress/>
                 }
            </div>
        );
    }
}

export default Anfragen;