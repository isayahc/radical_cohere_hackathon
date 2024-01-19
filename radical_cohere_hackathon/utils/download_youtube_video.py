import argparse
from pytube import YouTube

def download_youtube_video(url, output_path="."):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        print("Downloading:", yt.title)
        video_stream.download(output_path)
        print("Download complete!")

    except Exception as e:
        print("Error:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Download a YouTube video.")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", help="Output path (default is current directory)", default=".")

    args = parser.parse_args()

    # Call the function to download the YouTube video
    download_youtube_video(args.url, args.output)

if __name__ == "__main__":
    main()
