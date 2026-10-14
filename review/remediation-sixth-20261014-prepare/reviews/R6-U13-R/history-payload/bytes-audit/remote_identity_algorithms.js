
function utf8(s){
 const out=new Uint8Array(s.length*3);let n=0;
 for(let i=0;i<s.length;i++){let c=s.charCodeAt(i);
  if(c>=0xd800&&c<=0xdbff&&i+1<s.length){const d=s.charCodeAt(i+1);if(d>=0xdc00&&d<=0xdfff){c=0x10000+((c-0xd800)<<10)+(d-0xdc00);i++;}}
  if(c<0x80)out[n++]=c;
  else if(c<0x800){out[n++]=0xc0|(c>>6);out[n++]=0x80|(c&63);}
  else if(c<0x10000){out[n++]=0xe0|(c>>12);out[n++]=0x80|((c>>6)&63);out[n++]=0x80|(c&63);}
  else{out[n++]=0xf0|(c>>18);out[n++]=0x80|((c>>12)&63);out[n++]=0x80|((c>>6)&63);out[n++]=0x80|(c&63);}
 }return out.subarray(0,n);
}
const K256=[0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2];
function hash(data,kind){
 const size=Math.ceil((data.length+9)/64)*64;const p=new Uint8Array(size);p.set(data);p[data.length]=128;
 const high=Math.floor(data.length/0x20000000),low=(data.length*8)>>>0;
 for(let j=0;j<4;j++){p[size-8+j]=(high>>>(24-j*8))&255;p[size-4+j]=(low>>>(24-j*8))&255;}
 const w=new Uint32Array(80),h=kind===256?[0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19]:[0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0];
 const rr=(x,n)=>(x>>>n)|(x<<(32-n)),rl=(x,n)=>(x<<n)|(x>>>(32-n));
 for(let o=0;o<size;o+=64){
  for(let j=0;j<16;j++)w[j]=((p[o+j*4]<<24)|(p[o+j*4+1]<<16)|(p[o+j*4+2]<<8)|p[o+j*4+3])>>>0;
  if(kind===256){
   for(let j=16;j<64;j++){const x=w[j-15],y=w[j-2];w[j]=(w[j-16]+(rr(x,7)^rr(x,18)^(x>>>3))+w[j-7]+(rr(y,17)^rr(y,19)^(y>>>10)))>>>0;}
   let [a,b,c,d,e,f,g,z]=h;
   for(let j=0;j<64;j++){const t1=(z+(rr(e,6)^rr(e,11)^rr(e,25))+((e&f)^(~e&g))+K256[j]+w[j])>>>0;const t2=((rr(a,2)^rr(a,13)^rr(a,22))+((a&b)^(a&c)^(b&c)))>>>0;z=g;g=f;f=e;e=(d+t1)>>>0;d=c;c=b;b=a;a=(t1+t2)>>>0;}
   [a,b,c,d,e,f,g,z].forEach((v,j)=>h[j]=(h[j]+v)>>>0);
  }else{
   for(let j=16;j<80;j++)w[j]=rl(w[j-3]^w[j-8]^w[j-14]^w[j-16],1)>>>0;
   let [a,b,c,d,e]=h;
   for(let j=0;j<80;j++){let f,k;if(j<20){f=(b&c)|(~b&d);k=0x5a827999;}else if(j<40){f=b^c^d;k=0x6ed9eba1;}else if(j<60){f=(b&c)|(b&d)|(c&d);k=0x8f1bbcdc;}else{f=b^c^d;k=0xca62c1d6;}const t=(rl(a,5)+f+e+k+w[j])>>>0;e=d;d=c;c=rl(b,30);b=a;a=t;}
   [a,b,c,d,e].forEach((v,j)=>h[j]=(h[j]+v)>>>0);
  }
 }return h.map(v=>v.toString(16).padStart(8,"0")).join("");
}
function identity(content){
 const b=utf8(content);const prefix=utf8("blob "+b.length+"\0");const joined=new Uint8Array(prefix.length+b.length);joined.set(prefix);joined.set(b,prefix.length);
 return {bytes:b.length,sha256:hash(b,256),git_blob:hash(joined,1)};
}
function canonicalJSON(v){
 if(v===null||typeof v!=="object")return JSON.stringify(v);
 if(Array.isArray(v))return "["+v.map(canonicalJSON).join(",")+"]";
 return "{"+Object.keys(v).sort().map(k=>JSON.stringify(k)+":"+canonicalJSON(v[k])).join(",")+"}";
}
function canonical(v){return hash(utf8(canonicalJSON(v)),256);}
function ptr(v,p){for(const k of p.split("/").slice(1))v=v[k.replace(/~1/g,"/").replace(/~0/g,"~")];return v;}

