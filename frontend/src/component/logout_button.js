import { useHistory } from 'react-router-dom';
import Button from '@material-ui/core/Button';
import LogoutIcon from '@material-ui/icons/Close';

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
