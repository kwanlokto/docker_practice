import { useHistory } from 'react-router-dom';
import Button from '@material-ui/core/Button';

export const LogoutButton = () => {
  const history = useHistory();

  const handleLogout = () => {
    localStorage.removeItem('user.token');
    history.push('/login');
  };

  return (
    <Button onClick={handleLogout} variant="outlined">
      Logout
    </Button>
  );
};
