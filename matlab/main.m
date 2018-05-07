
data = load('data.arff');
size(data);
X=[data(:,1:17) data(:,19:19) data(:,21:26) data(:,28:28)];
size([data(:,1:17) data(:,19:19) data(:,21:26) data(:,28:28)]);
y=data(:,end:end);

test= load('test.arff');
Xtest=[test(:,1:17) test(:,19:19) test(:,21:26) test(:,28:28)];
ytest=test(:,end:end);
[m n]=size(X);
X = [ones(m, 1) X];
Xtest =[ones(999,1) Xtest];
initial_theta = zeros(n + 1, 1);
size(X)
options = optimset('GradObj', 'on', 'MaxIter', 1500);
 
[theta, cost] = ...
	fmincg(@(t)(costFunction(t, X, y)), initial_theta, options);

fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
fprintf(' %f \n', theta);
tp=0;
tn=0;
fp=0;
fn=0;
p = predict(theta, Xtest);

for i=1:length(ytest);
		if (ytest(i,1)==-1 && p(i,1)==0)
			tn++;
		elseif (ytest(i,1)==1 && p(i,1)==1)
			tp++;
		elseif(ytest(i,1)==-1 && p(i,1)==1)
			fp++;	
		elseif(ytest(i,1)==1 && p(i,1)==0)
			fn++;
		

end;



end;


[p(1:5,:),ytest(1:5,:)]

p=tp/(tp+fp);
r=tp/(tp+fn);
f1=2*p*r/(p+r);
error=(fp+fn)/(tp+tn+fp+fn);



fprintf(' Precision of model \n\n %f\n', p);
fprintf('Recall of model \n\n %f\n', r);
fprintf('F1 score of model \n\n %f\n', f1);
fprintf('Error Rate of model \n\n %f\n', error);


%data = load('output.txt');
%data=data'
%data = [1 data];
%p =predict(theta, data)
%theta
labels = {
'having_IP_Address'
'attribute URL_Length'
'Shortining_Service'
'having_At_Symbol  '
'double_slash_redirecting '
'Prefix_Suffix  '
'having_Sub_Domain  '
'SSLfinal_State  '
'Domain_registeration_length '
'Favicon'
'port'
'HTTPS_token '
'Request_URL '
'URL_of_Anchor '
'Links_in_tags '
'SFH  '
'Submitting_to_email '
'Abnormal_URL '
'Redirect  '
'on_mouseover '
'RightClick '
'popUpWidnow '
'Iframe'
'age_of_domain  '
'DNSRecord   '
'web_traffic  '
'Google_Index'
'Statistical_report '};
