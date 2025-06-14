import {
  Box,
  Button,
  Card,
  CardContent,
  Grid,
  IconButton,
  TextField,
  Typography,
} from '@material-ui/core';
import {
  createNewAccount,
  deleteAccount,
  getAllAccounts,
} from '../data-handler/auth';
import { useEffect, useState } from 'react';

import AddIcon from '@material-ui/icons/Add';
import DeleteIcon from '@material-ui/icons/Delete';
import { useHistory } from 'react-router-dom';
import { LogoutButton } from '../component/logout_button';

export const Dashboard = () => {
  const history = useHistory();

  const [accounts, setAccounts] = useState([]);
  const [newAccountName, setNewAccountName] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchAccounts = async () => {
    setLoading(true);
    try {
      const res = await getAllAccounts();
      setAccounts(res.data.data);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAccounts();
  }, []);

  const createAccount = async () => {
    if (!newAccountName.trim()) return;
    try {
      const res = await createNewAccount(newAccountName);
      setAccounts((prev) => [...prev, res.data.data]);
      setNewAccountName('');
    } catch (error) {
      console.error('Failed to create account', error);
    }
  };

  const removeAccount = (accountId) => {
    try {
      deleteAccount(accountId);
      setAccounts((prev) => prev.filter((acc) => acc.id !== accountId));
    } catch (error) {
      console.error('Failed to delete account', error);
    }
  };

  return (
    <Box sx={{ p: 4, maxWidth: 1000, mx: 'auto' }}>
      <Typography variant="h4" gutterBottom>
        Your Accounts
      </Typography>

      {loading ? (
        <Typography>Loading...</Typography>
      ) : (
        <Grid container spacing={2}>
          {accounts.map(({ id, name, balance }) => (
            <Grid item xs={12} sm={6} md={4} key={id}>
              <Card
                onClick={() => history.push(`/account/${id}`)}
                sx={{ cursor: 'pointer' }}
              >
                <CardContent>
                  <Box
                    display="flex"
                    justifyContent="space-between"
                    alignItems="center"
                  >
                    <Typography variant="h6">{name}</Typography>
                    <IconButton
                      onClick={(e) => {
                        e.stopPropagation();
                        removeAccount(id);
                      }}
                      size="small"
                      aria-label="delete account"
                    >
                      <DeleteIcon color="error" />
                    </IconButton>
                  </Box>
                  <Typography color="textSecondary">
                    Balance: ${balance}
                  </Typography>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}

      <Box mt={4} display="flex" gap={2} alignItems="center">
        <TextField
          label="New account name"
          value={newAccountName}
          onChange={(e) => setNewAccountName(e.target.value)}
          variant="outlined"
          size="small"
        />
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={createAccount}
          disabled={!newAccountName.trim()}
        >
          Create Account
        </Button>
      </Box>
      <LogoutButton />
    </Box>
  );
};
