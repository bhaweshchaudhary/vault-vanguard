import React, { useState } from 'react'

export default function App() {
    const [selectedFile, setSelectedFile] = useState(null);
  
    const handleFileChange = (event) => {
      setSelectedFile(event.target.files[0]);
    };

    const handleFileUpload = () => {
      const formData = new FormData();
      formData.append('file', selectedFile);
  
      fetch('http://your-django-server/api/encrypt-file', {
        method: 'POST',
        body: formData,
      })
        .then(response => response.text())
        .then(encryptedContent => {
          // Display the encrypted content in your React app
          console.log('Encrypted Content:', encryptedContent);
        })
        .catch(error => console.error('Error:', error));
    };


  return (
  <>

    <div className='w-[50%] h-[500px] mx-auto my-10 bg-[#F2F5F7] py-4 border-dashed border-[#B5C2CA] border'>

      <div className='hover:bg-slate-100'>

        <div className="py flex justify-center">
          <label htmlFor="file-upload" className='px-4 py-4 bg-[#9eb0bd] rounded-full cursor-pointer mt-10'>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-10 h-10 text-[#F2F5F7] bg-transparent">
              <path strokeLinecap="round" strokeLineJoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5" />
            </svg>
          </label>
          <input id="file-upload" type="file" className='hidden' onChange={handleFileChange} />
        </div>

        <div>
          <h1 className='text-[#4B5E6D] text-4xl mt-10 text-center'>
            Drag and drop files here
          </h1>
        </div>

        <div className='flex flex-row mt-20 justify-center'>
          <div className="border-t border-solid border-[#A7B7C3] h-2 w-32 mx-2 mt-3"></div>
          <span className="mx-2 text-[#A7B7C3]">or</span>
          <div className="border-t border-solid border-[#A7B7C3] h-2 w-32 mx-2 mt-3"></div>
        </div>

      </div>

      <label className='flex justify-center  mx-auto mt-10 p-3 bg-[#dbe3e7] w-40 rounded-md cursor-pointer text-[#32414B] font-semibold text-xl' htmlFor="browse-file">
        Browse Files
      </label>
      <input id="browse-file" type="file" className='hidden' onChange={handleFileChange} />

    </div>

  </>
  )
}