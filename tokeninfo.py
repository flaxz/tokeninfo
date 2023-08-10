import pandas as pd
from hiveengine.api import Api
from hiveengine.tokenobject import Token

api = Api(url = "https://engine.rishipanthee.com/")

token = input("Enter token symbol: ")

def main():
  
  tk = Token(token, api = api)
  tokenInfo = tk.get_info()
  decNum = tokenInfo["precision"]
  
  # print(tokenInfo)
  
  # Token supply
  supply = round(float(tokenInfo["supply"]), decNum)
  print("$"+token+" token supply: ",supply)
  
  # Token total stake
  stake = round(float(tokenInfo["totalStaked"]), decNum)
  print("$"+token+" token staked: ",stake)
  
  # Token burned
  burned = round(float(tokenInfo["supply"]) - float(tokenInfo["circulatingSupply"]), decNum)
  print("$"+token+" token burned: ",burned)
  
  # Token liquid
  liquid = round(float(tokenInfo["circulatingSupply"]) - float(tokenInfo["totalStaked"]), decNum)
  print("$"+token+" token liquid: ",liquid)
  
  # Token holders
  holders = api.find_all("tokens", "balances", query = {"symbol": token})
  
  df = pd.DataFrame(holders)
  df.drop(columns = ["_id", "balance", "pendingUnstake", "delegationsIn"], inplace = True)
  
  df["pendingUndelegations"] = df["pendingUndelegations"].astype(float)
  df["stake"] = df["stake"].astype(float)
  df["delegationsOut"] = df["delegationsOut"].astype(float)
  
  df = df.assign(ownedStake = df.sum(axis = 1, numeric_only = True))
  
  df["ownedStake"] = df["ownedStake"].round(decNum)
  
  indexZero = df[df["ownedStake"] == 0.0].index
  df.drop(indexZero, inplace = True)
  df.drop(columns = ["symbol", "stake", "delegationsOut", "pendingUndelegations"], inplace = True)
  
  df.sort_values(by=["ownedStake"], inplace = True, ascending = False)
  
  stakeHolders = len(df)
  print("Stake Holders:", stakeHolders, "$"+token, "stake holders.")
  
if __name__ == "__main__":
  
  main()
