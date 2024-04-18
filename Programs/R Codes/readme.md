Step to install R in your vscode editor 

1) Install R on device from [R website](https://cran.r-project.org/bin/windows/base/R-4.3.3-win.exe)

2) Install [R editor](https://marketplace.visualstudio.com/items?itemName=REditorSupport.r) extension from vs extenstion library

3) Add R in your Environment Path of windows
<img title="How to add Environment Path of R in Windows" alt="Search System Properties" src="https://github.com/GamingVj/first-repo/blob/8bc338dd259e38c57d25695e8652c9baaeeb83e0/Programs/assets/search%20system%20prop.png">
Then go to environment variable and add R path in system variable
<img title="sys prop" alt="System Properties" src="https://github.com/GamingVj/first-repo/blob/8bc338dd259e38c57d25695e8652c9baaeeb83e0/Programs/assets/sys%20prop.png">
<img title="envi path" alt="envi path" src="https://github.com/GamingVj/first-repo/blob/8bc338dd259e38c57d25695e8652c9baaeeb83e0/Programs/assets/envi%20path.png">

5) Open Rgui on your device and install the following packages

```
install.packages("languageserversetup")
languageserversetup::languageserver_install()
languageserversetup::languageserver_add_to_rprofile()
```

6) Now go to vscode extenstion setting of R and add the exec path R
<img title="R path vscode setting" alt="R Path vscode setting" src="https://github.com/GamingVj/first-repo/blob/8bc338dd259e38c57d25695e8652c9baaeeb83e0/Programs/assets/path%20vscode.png">

8) Create a R file and you should be able to run R code in vscode editor using shortcut key ```ALT+ENTER```.This will run code in R terminal
