import { useHistory } from 'react-router-dom';
import Button from '@mui/material/Button';
import LogoutIcon from '@mui/icons-material/Logout';

export const LogoutButton = () => {
  const history = useHistory();

  const handleLogout = () => {
    localStorage.removeItem('user.token');
    history.push('/login');
  };

  return (
    <Button
      onClick={handleLogout}
      variant="outlined"
      color="error"
      startIcon={<LogoutIcon />}
      sx={{ textTransform: 'none' }} // keeps "Logout" from being ALL CAPS
    >
      Logout
    </Button>
  );
};
