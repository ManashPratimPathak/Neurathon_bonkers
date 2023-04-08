import { useFilePicker } from "use-file-picker";
import "./../assets/styles/filePicker.css";
import React from "react";

export default function FilePickerButton() {
  const [openFileSelector, { filesContent, loading, errors }] = useFilePicker({
    readAs: "DataURL",
    accept: "image/*",
    multiple: true,
    limitFilesConfig: { max: 2 },
    // minFileSize: 1,
    maxFileSize: 50, // in megabytes
  });

  if (loading) {
    return <div>Loading...</div>;
  }

  if (errors.length) {
    return <div>Error...</div>;
  }

  return (
    <div>
      <button
        style={{
          backgroundColor: "transparent !important",
          border: "solid 1px white !important",
          borderRadius: "8px !important",
        }}
        className="filePicker_button"
        onClick={() => openFileSelector()}
      >
        Select files{" "}
      </button>
      <br />
      {filesContent.map((file, index) => (
        <div key={index}>
          <h2>{file.name}</h2>
          <img alt={file.name} src={file.content}></img>
          <br />
        </div>
      ))}
    </div>
  );
}
