import { LinearProgress } from '@mui/material';
import React, { Component } from 'react';
import BlockedProfileView from '../api/Views/BlockedProfileView';
import MatchCard from '../componnents/Matching/MatchCard';

class Blockiert extends Component {
    constructor(props) {
      super(props)

      this.state = {
         blockedList: [],
         loading: false

      }
    }



    getBlockedList = () =>{
        BlockedProfileView.getView().getByUserprofile_id(this.props.user.getID()).then(blockedList=>{
            this.setState({
                blockedList: blockedList,
                loading: false
            })
        })
        .catch((err) => console.log("error", err));
        this.setState({loading: true})
    }

    removeEntry = (entry) =>{
        this.setState({
            blockedList: this.state.blockedList.filter((item) => item.getID() !== entry.getID())
        })
    }

    componentDidMount() {
        this.getBlockedList()
        }
    render() {
        return (
            <div className='section-wrapper'>
                <div>
                    <h2 style={{color: "#E41036", margin:0}}>Blockierungen</h2>
                    <p>Diese Profile können dich nicht sehen und kontaktieren. Sie erscheinen auch nicht in deinen Matches!</p>
                </div>
                    {
                        !this.state.loading ?
                        <div className='section-card-grid'>
                       { this.state.blockedList.map((item)=>
                        <MatchCard parentComponent="blocked" key={item.getID()} user={this.props.user}
                        candidateID={item.getBlockeduserId()}
                        parentObject={item}
                        removeEntry={this.removeEntry}/>
                        )}
                </div>: <LinearProgress/>
                    }
            </div>
        );
    }
}

export default Blockiert;