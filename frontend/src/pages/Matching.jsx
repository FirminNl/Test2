import { LinearProgress } from '@mui/material';
import React, { Component } from 'react';
import MatchingView from '../api/Views/MatchingView';
import UserProfileView from '../api/Views/UserProfileView';
import MatchCard from '../componnents/Matching/MatchCard';
import Searchprofile from '../componnents/Matching/Searchprofile';
import "./Matchpage.css";

class Matching extends Component {
    constructor(props) {
        super(props)

        this.state = {
           matchList:[],
           isUnseen: false,
           loading: false
        }
      }


      getMatchList = () => {
        MatchingView.getView().getByUserProfileId(this.props.user.getID()).then((matchList)=>{
            this.setState({
              matchList: matchList,
              loading: false
            })
        })
        .catch((err) => {console.log(err)})
        this.setState({loading: true})
      }

      updateIsUnseen = (isUnseen) => {
        let newMatchList = []
        if(!isUnseen){
          newMatchList = this.state.matchList.filter((item) => item.getUnseenProfile() !== false)
        }
        else{
          this.getMatchList()
        }

        this.setState({
          isUnseen: isUnseen,
          matchList: newMatchList
        })
      }
      removeEntry = (entry) => {
        this.setState({
          matchList: this.state.matchList.filter((item) => item.getID() !== entry.getID() )
        })
      }

      refreshMatches = () => {
        this.setState({
          matchList: []
        })
        this.getMatchList()
      }

      componentDidMount(){
        this.getMatchList()
      }
    render() {
        return (
            <div className='section-wrapper'>
                <div>
                    <h2 style={{color: "#E41036", margin:0}}>Matching</h2>
                    <p>Passe dein Suchprofil an, sodass unser HeyDateMe-Algorithmus passende Matches zu dir findet! </p>
                    <Searchprofile refreshMatches={this.refreshMatches} user={this.props.user} updateIsUnseen={this.updateIsUnseen}/>
                </div>
                {!this.state.loading ?
                <div className='section-card-grid'>
               { this.state.matchList.map((match) =>
                <MatchCard
                refreshMatches={this.refreshMatches}
                parentComponent="match"
                key={match.getID()}
                parentObject={match} user={this.props.user} removeEntry={this.removeEntry} candidateID={match.getCandidateprofileId()}
                 />
                )}</div>
                :<LinearProgress/>}
            </div>
        );
    }
}


export default Matching;