function  setsimenv





















 restoredefaultpath;
 fprintf( 'Add simulation path.\n');


 verRelDate= '2018-12-04';
 RelDateNum= datenum( verRelDate);


 rootPath= fileparts( mfilename( 'fullpath'));
 changeFlag= 0;


 changeFlag= addPath_checkFileChangeInFolder( rootPath, RelDateNum, changeFlag, 0);


 select_subFolder={
 'analysis';
 'config';
 'database';
 'dsp';
 'input';
 'lib';
 'logs';
 'math';

 'output';
 'ref';
 'results';
 'scripts';
 'tools';
 'utility';
};

 num_sub= length( select_subFolder);

for  isub= 1: num_sub
 subfolderName= fullfile( rootPath, select_subFolder{ isub});
 changeFlag= addPath_checkFileChangeInFolder( subfolderName, RelDateNum, changeFlag, 1);
end


 dataBasePath= fullfile( rootPath, 'database');
 dataBaseFullPath= fullfile( dataBasePath, 'rootPath.mat');
if ~ checkDirExist( dataBasePath)
 mkdir( dataBasePath);
 addpath( dataBasePath);
end
 save( dataBaseFullPath, 'rootPath');




end



function  changeFlag= addPath_checkFileChangeInFolder( folderName, RelDateNum, changeFlag, subFolderFlag)

 addpath( folderName);
 fileList= dir( folderName);

for  fileNdx= 3: length( fileList)
if  fileList( fileNdx). isdir
if ( subFolderFlag== 1)
 changeFlag= addPath_checkFileChangeInFolder( fullfile( folderName, fileList( fileNdx). name),
 RelDateNum, changeFlag, subFolderFlag);
end
else 
if  floor( fileList( fileNdx). datenum)> RelDateNum
 fprintf( '%-30s%s \n', fileList( fileNdx). date, fullfile( folderName, fileList( fileNdx). name));
 changeFlag= 1;
end
end
end
end