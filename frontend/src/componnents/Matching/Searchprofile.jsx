import { Button, FormControlLabel, Switch } from '@mui/material'
import React, { Component } from 'react'
import SearchProfileBO from "../../api/SearchProfileBO"
import { default as SearchProfileView, default as SearchprofileView } from "../../api/Views/SearchProfileView"
import "./Matching.css"
import SearchprofileDialog from './SearchprofileDialog'
export class Searchprofile extends Component {
    constructor(props) {
      super(props)

      this.state = {
        searchprofile: null,
        spNotExisting: false,
        isUnseen: false,
        loading: false,
        openSearchprofileDialog: false
      }
    }

    getSearchprofile = () => {
        SearchprofileView.getView().getByUserprofileId(this.props.user.getID()).then((searchprof) =>{
            this.setState({
              searchprofile: searchprof[0],
              spNotExisting: searchprof[0].getID() ? false : true
            })
        })
        .catch((err) => console.log("error", err));
    }

    handleSwitchChange = (event) => {
      this.setState({
        isUnseen: event.target.checked,
      })
      this.props.updateIsUnseen(this.state.isUnseen)
    }

    openSearchprofileDialog = () => {
      if(this.state.spNotExisting){

        let newSearchprofile = new SearchProfileBO(this.props.user.getID())
        SearchProfileView.getView().create(newSearchprofile).then((searchprofile) => {
          this.setState({
            loading: false,
            openSearchprofileDialog: true,
            searchprofile: searchprofile,
            spNotExisting: false
          })
        })
        .catch((err) => console.log("error", err));
      }
      else{
        this.setState({
          openSearchprofileDialog: true
        })
      }
      this.setState({
        loading: true
      })
    }

    handleCloseSearchprofileDialog = () => {
      this.setState({
        openSearchprofileDialog: false
      })
      this.props.refreshMatches()
    }

    componentDidMount() {
        this.getSearchprofile()
    }

  render() {
    return (
      <div className='searchprofile-wrapper'>
            <Button
            variant="contained"
            onClick={this.openSearchprofileDialog}>
                {
                    this.state.spNotExisting ?
                    this.state.loading ?
                    "Loading..." :
                    "Suchprofil erstellen"
                    : "Suchprofil bearbeiten"
                }
            </Button>
            <div className='anfragen-button-group'>
                        <p>Alle</p>
                        <Switch
                        checked={this.state.isUnseen}
                        onChange={this.handleSwitchChange}
                        />
                        <p>Nicht angesehene</p>
                    </div>
        <div>
        </div>
        <SearchprofileDialog user={this.props.user} searchprofile={this.state.searchprofile} openSearchprofileDialog={this.state.openSearchprofileDialog} closeSearchprofileDialog={this.handleCloseSearchprofileDialog}/>
      </div>
    )
  }
}

export default Searchprofile