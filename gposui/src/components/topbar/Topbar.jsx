import React from "react";
import Style from "./topbar.module.css";
import { HiMagnifyingGlass } from "react-icons/hi2";
import IconButton from "@mui/material/IconButton";
import Tooltip from "@mui/material/Tooltip";
import NotificationsActiveIcon from "@mui/icons-material/NotificationsActive";
import MarkEmailUnreadIcon from "@mui/icons-material/MarkEmailUnread";
import Badge from "@mui/material/Badge";
import Avatar from '@mui/material/Avatar';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';

function Topbar() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };
  return (
    <div className={Style.topbar}>
      <div className={Style.searchItem}>
        <input
          className={Style.search}
          type="text"
          placeholder="Search here.."
        />
        <span>
          <HiMagnifyingGlass />
        </span>
      </div>
      <div className={Style.topItem}>
        <Tooltip title="Email">
          <IconButton className={Style.navbtn}>
            <Badge badgeContent={4} color="error">
              <MarkEmailUnreadIcon />
            </Badge>
          </IconButton>
        </Tooltip>
        <Tooltip title="Notification">
          <IconButton className={Style.navbtn}>
            <Badge badgeContent={4} color="error">
              <NotificationsActiveIcon />
            </Badge>
          </IconButton>
        </Tooltip>
        <Tooltip title="Account settings">
          <IconButton 
            className={Style.userProfile}
            onClick={handleClick}
            size="small"
            sx={{ ml: 2 }}
            aria-controls={open ? 'account-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={open ? 'true' : undefined}
          >
            <Avatar sx={{ width: 32, height: 32 }}>M</Avatar>
          </IconButton>
        </Tooltip>
        <Menu
        anchorEl={anchorEl}
        id="account-menu"
        open={open}
        onClose={handleClose}
        onClick={handleClose}
        PaperProps={{
          elevation: 0,
          sx: {
            overflow: 'visible',
            filter: 'drop-shadow(0px 2px 8px rgba(0,0,0,0.32))',
            mt: 1.5,
            '& .MuiAvatar-root': {
              width: 32,
              height: 32,
              ml: -0.5,
              mr: 1,
            },
            '&:before': {
              content: '""',
              display: 'block',
              position: 'absolute',
              top: 0,
              right: 14,
              width: 10,
              height: 10,
              // bgcolor: 'background.paper',
              transform: 'translateY(-50%) rotate(45deg)',
              zIndex: 0,
            },
          },
        }}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        <MenuItem onClick={handleClose} className={Style.topItemProfile}>
          <Avatar /> <span>Profile</span>
        </MenuItem>
        <MenuItem onClick={handleClose} className={Style.topItemProfile}>
          <Avatar /><span>My account</span> 
        </MenuItem>
      </Menu>

       

      </div>
    </div>
  );
}

export default Topbar;
