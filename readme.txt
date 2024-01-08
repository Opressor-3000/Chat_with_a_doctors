


git checkout yusif 
&& 
git add . && git commit -m 'install pydantic-settings' 
&& 
git push origin yusif 
&& 
git checkout dev && git merge origin yusif && git checkout yusif 

run server 

uvicorn main:app --reload 


