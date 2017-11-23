package com.company;

import org.apache.commons.io.FilenameUtils;
import org.apache.commons.io.IOUtils;
import org.jetbrains.annotations.NotNull;

import java.io.*;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipInputStream;

import static java.lang.System.out;

public class FileZip {
    private static FileZip instance = null;

    private FileZip() {

    }

    public synchronized static FileZip getInstance() {
        if (instance == null)
            instance = new FileZip();
        return instance;
    }

    @NotNull
    private File getFile(String path) {
        return new File( path );
    }

    @NotNull
    private FileInputStream getInputStream(File file) throws FileNotFoundException {
        return new FileInputStream( file );
    }

    @NotNull
    private BufferedReader getReader(InputStream inputStream) {
        return new BufferedReader( new InputStreamReader( inputStream ) );
    }

    @NotNull
    private ZipInputStream getZipInputStream(InputStream inputStream) {
        return new ZipInputStream( inputStream );
    }


    public boolean unZipFile(File input, File output) throws FileFormatException, IOException {
        byte[] buffer = new byte[1024];
        if (!output.exists()) {
            boolean isCreated = output.mkdir();
        }
        output=new File( output,input.getName().substring( 0,input.getName().lastIndexOf( "." ) ) );

        if (!FilenameUtils.getExtension( input.getPath() ).equalsIgnoreCase( "zip" ))
            throw new FileFormatException();
        ZipFile zipFile = new ZipFile( input );
        try {
            Enumeration<? extends ZipEntry> entries = zipFile.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = entries.nextElement();
                File entryDestination = new File( output, entry.getName() );
                if (entry.isDirectory()) {
                    boolean b = entryDestination.mkdirs();
                    System.out.println(b);
                } else {
                    entryDestination.getParentFile().mkdirs();
                    InputStream in = zipFile.getInputStream( entry );
                    OutputStream out = null;

                         out = new FileOutputStream( entryDestination );

                    IOUtils.copy( in, out );
                    IOUtils.closeQuietly( in );
                    out.close();
                }
            }
        } finally {
            zipFile.close();
        }
        return true;

    }






}
