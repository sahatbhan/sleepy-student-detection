import * as React from 'react'
import PropTypes from 'prop-types'
import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import CssBaseline from '@mui/material/CssBaseline'
import Divider from '@mui/material/Divider'
import Drawer from '@mui/material/Drawer'
import IconButton from '@mui/material/IconButton'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import ListItemIcon from '@mui/material/ListItemIcon'
import ListItemText from '@mui/material/ListItemText'
import MenuIcon from '@mui/icons-material/Menu'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import DashboardIcon from '@mui/icons-material/Dashboard'
import { useNavigate } from "react-router";
import logo from '../Images/logo.png'
import '../Assets/Sidebar.css'

const drawerWidth = 240

function ResponsiveDrawer(props) {
    let navigate = useNavigate()

    const { windows } = props
    const [mobileOpen, setMobileOpen] = React.useState(false)
    const { children } = props



    const handleDrawerToggle = () => {
        setMobileOpen(!mobileOpen)
    }

    const drawer = (
        <div>
            <Box className="logoBox">
                <img src={logo} className="logo" />
            </Box>
            <Divider />
            <List>
                <ListItem button onClick={() => navigate('/')}>
                    <ListItemIcon>
                        <DashboardIcon />
                    </ListItemIcon>
                    <ListItemText
                        sx={{ color: '#000', textDecoration: 'none!important' }}
                        primary="Dashboard"
                    />
                </ListItem>
            </List>
            {/* <Divider />
            <List>
                <ListItem button onClick={() => navigate('/webinars')}>
                    <ListItemIcon>
                        <CalendarMonthIcon />
                    </ListItemIcon>
                    <ListItemText primary="Webinars" />
                </ListItem>
            </List>
            <Divider />
            <List>
                <ListItem button onClick={() => navigate('/news')}>
                    <ListItemIcon>
                        <NewspaperIcon />
                    </ListItemIcon>
                    <ListItemText primary="News/Podcasts" />
                </ListItem>
            </List>
            <Divider />
            <List>
                <ListItem button onClick={() => navigate('/support')}>
                    <ListItemIcon>
                        <ContactSupportIcon />
                    </ListItemIcon>
                    <ListItemText primary="Support" />
                </ListItem>
            </List> */}
        </div>
    )

    const container =
        windows !== undefined ? () => windows().document.body : undefined

    return (
        <Box sx={{ display: 'flex' }}>
            <CssBaseline />

            <Box
                component="nav"
                sx={{ width: { sm: drawerWidth }, flexShrink: { sm: 0 } }}
                aria-label="mailbox folders"
            >
                <Drawer
                    container={container}
                    variant="temporary"
                    open={mobileOpen}
                    onClose={handleDrawerToggle}
                    ModalProps={{
                        keepMounted: true,
                    }}
                    sx={{
                        display: { xs: 'block', sm: 'none' },
                        '& .MuiDrawer-paper': {
                            boxSizing: 'border-box',
                            width: drawerWidth,
                            borderRadius: '20px'
                        },
                    }}
                >
                    {drawer}
                </Drawer>
                <Drawer
                    variant="permanent"
                    sx={{
                        display: { xs: 'none', sm: 'block' },
                        '& .MuiDrawer-paper': {
                            boxSizing: 'border-box',
                            width: drawerWidth,
                        },
                    }}
                    open
                >
                    {drawer}
                </Drawer>
            </Box>
            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    p: 3,
                    width: { sm: `calc(100% - ${drawerWidth}px)` },
                    backgroundColor: '#E8EAED',
                }}
            >
                <Toolbar />
                {children}
            </Box>
        </Box>
    )
}

ResponsiveDrawer.propTypes = {
    windows: PropTypes.func,
}

export default ResponsiveDrawer