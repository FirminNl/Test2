import { LinearProgress } from '@mui/material';
import React, { Component } from 'react';
import MemoBoardView from '../api/Views/MemoBoardView';
import MatchCard from '../componnents/Matching/MatchCard';

class Merkliste extends Component {
    constructor(props) {
      super(props)

      this.state = {
         memoList: [],
         loading: false
      }
    }

    getMemoList = () =>{
        MemoBoardView.getView().getByUserprofile_id(this.props.user.getID()).then(memoList=>{
            this.setState({
                memoList: memoList,
                loading: false
            })
        })
        .catch((err) => console.log("error", err));
        this.setState({
            loading: true
        })
    }

    removeEntry = (entry) =>{
        this.setState({
            memoList: this.state.memoList.filter((item) => item.getID() !== entry.getID())
        })
    }

    componentDidMount() {
    this.getMemoList()
    }
    render() {
        return (
            <div className='section-wrapper'>
                <div>
                    <h2 style={{color: "#E41036", margin:0}}>Merkliste</h2>
                    <p>In deiner Merkliste kannst du Profile aus deinem Matching speichern, die du später anschreiben oder ansehen möchtest!</p>
                </div>
                    {
                        !this.state.loading ?
                <div className='section-card-grid'>
                        {this.state.memoList.map((item)=>
                        <MatchCard parentComponent="marked" key={item.getID()} user={this.props.user}
                        candidateID={item.getSavedId()}
                        parentObject={item}
                        removeEntry={this.removeEntry}/>
                        )}
                </div>
                : <LinearProgress/>
                    }
            </div>
        );
    }
}

export default Merkliste;