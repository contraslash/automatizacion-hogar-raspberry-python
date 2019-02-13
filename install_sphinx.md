# Install Sphinx 

For OSX users
```bash
brew install autoconf automake libtool
brew install swig
```

For  Ubuntu USers
```bash
sudo apt install autoconf
sudo apt install swig
```

Clone the projects and build the projects
```bash
git clone https://github.com/cmusphinx/sphinxbase
git clone https://github.com/cmusphinx/sphinxtrain
git clone https://github.com/cmusphinx/pocketsphinx

cd sphinxbase
./autogen.sh
make 
sudo make install

cd ../sphinxtrain
./autogen.sh
make 
sudo make install

cd ../pocketsphinx
./autogen.sh
make 
sudo make install
```


Troubleshooting OSX

configure: error: OpenAL not found

```bash
xcode-select --install
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```