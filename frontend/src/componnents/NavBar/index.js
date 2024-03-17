import ForumIcon from "@mui/icons-material/Forum";
import LocalFireDepartmentIcon from "@mui/icons-material/LocalFireDepartment";
import LogoutIcon from "@mui/icons-material/Logout";
import MarkChatUnreadIcon from "@mui/icons-material/MarkChatUnread";
import MenuIcon from "@mui/icons-material/Menu";
import MenuOpenIcon from "@mui/icons-material/MenuOpen";
import PersonIcon from "@mui/icons-material/Person";
import RemoveCircleIcon from "@mui/icons-material/RemoveCircle";
import StarIcon from "@mui/icons-material/Star";
import { IconButton } from "@mui/material";
import React, { useState } from "react";
import { Link } from "react-router-dom";
import headline from "../../media/HeyDateMe_Logo.png";
import logo from "../../media/heydatemelogo.svg";
import "./NavBar.css";
import ProfileDropDown from "./ProfileDropDown";

const pages = [
  {
    id: 1,
    name: "Mein Profil",
    route: "Profil",
  },
  {
    id: 2,
    name: "Matches",
    route: "Matching",
  },
  {
    id: 3,
    name: "Chatanfragen",
    route: "Anfragen",
  },
  {
    id: 4,
    name: "Chats",
    route: "Chats",
  },
  {
    id: 5,
    name: "Blockierte Profile",
    route: "Blockiert",
  },
  {
    id: 6,
    name: "Merkliste",
    route: "Merkliste",
  },
];
const settings = ["Logout", "Name", "email"];
const NavBar = ({ user, isSavedProp, fnSaved }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleLinkCliked = () => {
    if (isSavedProp) {
      alert("Du hast vergessen deine Eigenschaften zu speichern!");
    }
    if (fnSaved) {
      alert("Bitte geb einen Namen ein!");
    }

    setIsOpen(!isOpen);
  };

  return (
    <div>
      <div
        style={{
          width: "100vw",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <img className="nav-img" src={headline} alt="headline"></img>
      </div>
      <nav
        className="navbar"
        style={{
          transform: `translateX(${isOpen ? "0" : "-233px"})`,
          position: "fixed",
          background: isOpen
            ? "linear-gradient(180deg, #E9E9E9 0%, #FFFFFF 73.44%)"
            : "none",
          zIndex: isOpen ? "10" : "0",
        }}
      >
        <div className="navbar-wrapper">
          <IconButton
            onClick={() => setIsOpen(!isOpen)}
            sx={{ position: "absolute", top: 10, right: 25 }}
          >
            {isOpen ? (
              <MenuOpenIcon fontSize="large" />
            ) : (
              <MenuIcon fontSize="large" />
            )}
          </IconButton>
          <div style={{ position: "relative" }}>
            <img
              src={logo}
              alt="Logo"
              style={{
                width: "140px",
                height: "auto",
                marginBottom: "45px",
              }}
            />
            <div style={{ position: "absolute", top: "25%", left: "30%" }}>
              <ProfileDropDown user={user} />
            </div>
          </div>
          <ul className="nav-list">
            <li className="nav-item">
              <PersonIcon
                sx={{
                  color: "#E41036",
                  fontSize: "42px",
                  paddingRight: "30px",
                }}
              />
              <Link
                to={fnSaved ? null : isSavedProp ? null : "/Profil"}
                className="link-item"
                onClick={handleLinkCliked}
              >
                Profil
              </Link>
            </li>
            <li className="nav-item">
              <LocalFireDepartmentIcon
                sx={{
                  color: "#E41036",
                  fontSize: "42px",
                  paddingRight: "30px",
                }}
              />
              <Link
                to={fnSaved ? null : isSavedProp ? null : "/Matching"}
                className="link-item"
                onClick={handleLinkCliked}
              >
                Matching
              </Link>
            </li>
            <li className="nav-item">
              <MarkChatUnreadIcon
                sx={{
                  color: "#E41036",
                  fontSize: "42px",
                  paddingRight: "30px",
                }}
              />
              <Link
                to={fnSaved ? null : isSavedProp ? null : "/Anfragen"}
                className="link-item"
                onClick={handleLinkCliked}
              >
                Anfragen
              </Link>
            </li>
            <li className="nav-item">
              <ForumIcon
                sx={{
                  color: "#E41036",
                  fontSize: "42px",
                  paddingRight: "30px",
                }}
              />
              <Link
                to={fnSaved ? null : isSavedProp ? null : "/Chats"}
                className="link-item"
                onClick={handleLinkCliked}
              >
                Chats
              </Link>
            </li>
            <li className="nav-item">
              <RemoveCircleIcon
                sx={{
                  color: "#E41036",
                  fontSize: "42px",
                  paddingRight: "30px",
                }}
              />
              <Link
                to={fnSaved ? null : isSavedProp ? null : "/Blockiert"}
                className="link-item"
                onClick={handleLinkCliked}
              >
                Blockiert
              </Link>
            </li>
            <li className="nav-item">
              <StarIcon
                sx={{
                  color: "#E41036",
                  fontSize: "42px",
                  paddingRight: "30px",
                }}
              />
              <Link
                to={fnSaved ? null : isSavedProp ? null : "/Merkliste"}
                className="link-item"
                onClick={handleLinkCliked}
              >
                Merkliste
              </Link>
            </li>
          </ul>
        </div>
      </nav>
    </div>
  );
};

export default NavBar;
