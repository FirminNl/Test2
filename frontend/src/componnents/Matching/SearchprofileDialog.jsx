import CloseIcon from "@mui/icons-material/Close";
import { AppBar, Button, Dialog, DialogContent, DialogTitle, IconButton, Slide, Toolbar, Typography } from '@mui/material';
import React, { Component } from 'react';
import Eigenschaften from "../Profile/Eigenschaften";

const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});
export class SearchprofileDialog extends Component {
    constructor(props) {
      super(props)

      this.state = {

      }
    }

    handleCloseSearchprofileDialog = () => {
        this.props.closeSearchprofileDialog()
    }
  render() {
    return (
      <Dialog open={this.props.openSearchprofileDialog} fullScreen TransitionComponent={Transition}>
        <AppBar sx={{ position: 'relative' }}>
          <Toolbar>
            <IconButton
              edge="start"
              color="inherit"
              onClick={this.handleCloseSearchprofileDialog}
              aria-label="close"
            >
              <CloseIcon />
            </IconButton>
            <Typography sx={{ ml: 2, flex: 1 }} variant="h6" component="div">
              Suchprofil
            </Typography>
          </Toolbar>
        </AppBar>
        <DialogContent>
            <Eigenschaften profile={this.props.searchprofile} isSearchprofile={true} user={this.props.user}/>
        </DialogContent>
      </Dialog>
    )
  }
}

export default SearchprofileDialog