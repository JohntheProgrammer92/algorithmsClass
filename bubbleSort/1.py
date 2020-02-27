def group_by_owners(files):
  output = {}
  for i in files:
    print(i)
    owner = files[i]
    print(owner)
    if owner in output:
      output[owner].append(i)
    else:
      output[owner] = [i]
      print(output)
   


  return output

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))