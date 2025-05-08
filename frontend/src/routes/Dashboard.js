import {
  Box,
  Button,
  Card,
  CardContent,
  Grid,
  IconButton,
  TextField,
  Typography
} from "@material-ui/core";
import React, { useState } from "react";

import AddIcon from '@material-ui/icons/Add';
import DeleteIcon from '@material-ui/icons/Delete';

export const Dashboard = () => {
  const [accounts, setAccounts] = useState([
    { id: 1, name: "Checking", balance: 1200.5 },
    { id: 2, name: "Savings", balance: 5500.75 },
  ]);
  const [newAccountName, setNewAccountName] = useState("");

  const createAccount = () => {
    if (!newAccountName.trim()) return;
    const newAccount = {
      id: Date.now(),
      name: newAccountName,
      balance: 0.0,
    };
    setAccounts([...accounts, newAccount]);
    setNewAccountName("");
  };

  const removeAccount = (id) => {
    setAccounts(accounts.filter((acc) => acc.id !== id));
  };

  return (
    <Box sx={{ p: 4, maxWidth: 1000, mx: "auto" }}>
      <Typography variant="h4" gutterBottom>
        Your Accounts
      </Typography>

      <Grid container spacing={2}>
        {accounts.map((account) => (
          <Grid item xs={12} sm={6} md={4} key={account.id}>
            <Card>
              <CardContent>
                <Box display="flex" justifyContent="space-between" alignItems="center">
                  <Typography variant="h6">{account.name}</Typography>
                  <IconButton onClick={() => removeAccount(account.id)}>
                    <DeleteIcon color="error" />
                  </IconButton>
                </Box>
                <Typography color="textSecondary">
                  Balance: ${account.balance.toFixed(2)}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      <Box mt={4} display="flex" gap={2} alignItems="center">
        <TextField
          label="New account name"
          value={newAccountName}
          onChange={(e) => setNewAccountName(e.target.value)}
        />
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={createAccount}
        >
          Create Account
        </Button>
      </Box>
    </Box>
  );
};
