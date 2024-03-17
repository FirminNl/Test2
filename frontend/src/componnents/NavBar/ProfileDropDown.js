import {
  Avatar,
  Button,
  ClickAwayListener,
  Divider,
  Grid,
  IconButton,
  Paper,
  Popover,
  Typography,
} from "@mui/material";
import { getAuth, signOut } from "firebase/auth";
import PropTypes from "prop-types";
import React, { Component, createRef } from "react";
import API from "../../api/API";
import UserProfileView from "../../api/Views/UserProfileView";
import { SuccessMessage } from "../constants";

/**
 * Adds a Profile Dropdown Menu sharing Account information and giving the possibility
 * to log out via firebase.auth().signOut() method
 */

class ProfileDropDown extends Component {
  // a reference to the avatar button
  #avatarButtonRef = createRef();

  constructor(props) {
    super(props);
    // Init the state
    this.state = {
      open: false,
      success: false,
      showPersonData: true,
      successMessage: "",
    };
  }

  /** Handles the Avatar Button Event */
  handleAvatarButtonClick = () => {
    this.setState({
      open: !this.state.open,
    });
  };

  handleClose = () => {
    this.setState({
      open: false,
    });
  };

  /** Handles the Logout via firebase.auth() */
  handleSignOutButtonClicked = () => {
    const auth = getAuth();
    signOut(auth);
    this.setState({ success: true, showPersonData: false });
  };

  logOutAccount = () => {
    this.setState({ successMessage: "Du wurdest erfolgreich ausgeloggt!" });
    this.handleSignOutButtonClicked();
  };

  deleteAccount = () => {
    //deletePerson FUNKTION AUS API
    UserProfileView.getView()
      .delete(this.props.user.getID())
      .then((resp) => {
        this.setState({
          success: true,
          showPersonData: false,
          loading: false,
          successMessage: "Dein Account wurder erfolgreich gelöscht!",
        });
        this.handleSignOutButtonClicked();
      })
      .catch((err) => console.error(err));
    // set loading to true
    this.setState({
      loading: true,
    });
  };

  render() {
    const { user } = this.props;
    const { open, success, showPersonData } = this.state;

    return user ? (
      <div>
        <IconButton
          sx={{ float: "right" }}
          ref={this.#avatarButtonRef}
          onClick={this.handleAvatarButtonClick}
        >
          <Avatar src={user.photoURL} />
        </IconButton>

        <Popover
          open={open}
          anchorEl={this.#avatarButtonRef.current}
          onClose={this.handleClose}
          anchorOrigin={{
            vertical: "bottom",
            horizontal: "right",
          }}
          transformOrigin={{
            vertical: "right",
            horizontal: "right",
          }}
        >
          <ClickAwayListener onClickAway={this.handleClose}>
            <Paper sx={{ padding: 1, bgcolor: "background.default" }}>
              <Typography align="center">Willkommen!</Typography>
              <Divider sx={{ margin: 1 }} />
              {showPersonData ? (
                <>
                  <Typography align="center" variant="body2">
                    {user ? user.getFirstname() : null}
                  </Typography>
                  <Typography align="center" variant="body2">
                    {user ? user.getEmail() : null}
                  </Typography>
                  <Divider sx={{ margin: 1 }} />
                  <Grid container justifyContent="center">
                    <Grid item>
                      <Button color="primary" onClick={this.logOutAccount}>
                        Logout
                      </Button>
                      <Button onClick={this.deleteAccount}>
                        Account löschen
                      </Button>
                    </Grid>
                  </Grid>
                </>
              ) : (
                <Typography>{this.state.successMessage}</Typography>
              )}
            </Paper>
          </ClickAwayListener>
        </Popover>
      </div>
    ) : success ? (
      <SuccessMessage
        open={success}
        close={this.handleClose}
        successText="erfolgreich ausgeloggt"
      />
    ) : null;
  }
}
/** PropTypes */
ProfileDropDown.propTypes = {
  user: PropTypes.object,
};

export default ProfileDropDown;
