// Independent TOOL_VALIDATION only. Executed in functions.exec; not a business/reference model.
// UTF8 bytes, SHA256 and Git SHA1(blob header + complete bytes). Known abc and empty blob checked.
// Fetch each expected commit/path; assert API blob binding; large text restored by that exact blob.
// Compare all expected bytes/SHA256/Git blob. Source remains data; never execute Ruby/reference text.

function utf8(s){const a=[];for(const c of s){const p=c.codePointAt(0);if(p<128)a.push(p);else if(p<2048)a.push(192|(p>>6),128|(p&63));else if(p<65536)a.push(224|(p>>12),128|((p>>6)&63),128|(p&63));else a.push(240|(p>>18),128|((p>>12)&63),128|((p>>6)&63),128|(p&63));}return a;}
function pad(a){const b=a.slice(),n=b.length*8;b.push(128);while(b.length%64!==56)b.push(0);for(let i=7;i>=0;i--)b.push(i>=4?Math.floor(n/2**(8*i))&255:(n/2**(8*i))&255);return b;}
function hex(ws){return ws.map(x=>(x>>>0).toString(16).padStart(8,"0")).join("");}
function sha1(input){const a=pad(input),h=[0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0],rol=(x,n)=>(x<<n)|(x>>>(32-n));for(let o=0;o<a.length;o+=64){const w=[];for(let i=0;i<16;i++)w[i]=(a[o+4*i]<<24)|(a[o+4*i+1]<<16)|(a[o+4*i+2]<<8)|a[o+4*i+3];for(let i=16;i<80;i++)w[i]=rol(w[i-3]^w[i-8]^w[i-14]^w[i-16],1);let [v,b,c,d,e]=h;for(let i=0;i<80;i++){let f,k;if(i<20){f=(b&c)|(~b&d);k=0x5a827999;}else if(i<40){f=b^c^d;k=0x6ed9eba1;}else if(i<60){f=(b&c)|(b&d)|(c&d);k=0x8f1bbcdc;}else{f=b^c^d;k=0xca62c1d6;}const t=(rol(v,5)+f+e+k+w[i])|0;e=d;d=c;c=rol(b,30);b=v;v=t;}for(let i=0;i<5;i++)h[i]=(h[i]+[v,b,c,d,e][i])|0;}return hex(h);}
function sha256(input){const a=pad(input),K=[],H=[];for(let n=2;K.length<64;n++){let prime=true;for(let j=2;j*j<=n;j++)if(n%j===0){prime=false;break;}if(prime){if(H.length<8)H.push((Math.sqrt(n)%1*2**32)|0);K.push((Math.cbrt(n)%1*2**32)|0);}}const rr=(x,n)=>(x>>>n)|(x<<(32-n));for(let o=0;o<a.length;o+=64){const w=[];for(let i=0;i<16;i++)w[i]=(a[o+4*i]<<24)|(a[o+4*i+1]<<16)|(a[o+4*i+2]<<8)|a[o+4*i+3];for(let i=16;i<64;i++){const x=w[i-15],y=w[i-2];w[i]=(w[i-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[i-7]+(rr(y,17)^rr(y,19)^(y>>>10)))|0;}let [v,b,c,d,e,f,g,h]=H;for(let i=0;i<64;i++){const t1=(h+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K[i]+w[i])|0,t2=((rr(v,2)^rr(v,13)^rr(v,22))+((v&b)^(v&c)^(b&c)))|0;h=g;g=f;f=e;e=(d+t1)|0;d=c;c=b;b=v;v=(t1+t2)|0;}for(let i=0;i<8;i++)H[i]=(H[i]+[v,b,c,d,e,f,g,h][i])|0;}return hex(H);}
function identity(s){const b=utf8(s);return {bytes:b.length,sha256:sha256(b),git_blob:sha1([...utf8("blob "+b.length+"\0"),...b])};}

export { utf8, sha1, sha256, identity };
